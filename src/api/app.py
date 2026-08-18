"""FastAPI application for Enterprise Data Ontology Knowledge Graph API & Dashboard"""

from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from src.ontology.ontology_builder import OntologyBuilder
from src.knowledge_graph.graph_manager import KnowledgeGraphManager
from src.utils.validators import validate_entity, validate_relationship

# Global instances
ontology_store = OntologyBuilder()
graph_store = KnowledgeGraphManager()

def populate_sample_data():
    """Populate default enterprise data ontology and graph"""
    ontology_store.clear()

    # Entities
    ontology_store.add_entity("E-001", "Customer", {"name": "Acme Corp", "segment": "Enterprise", "revenue": "$12M", "region": "North America"})
    ontology_store.add_entity("E-002", "Customer", {"name": "GlobalTech Inc", "segment": "Enterprise", "revenue": "$45M", "region": "Europe"})
    ontology_store.add_entity("E-003", "Order", {"order_number": "ORD-9921", "amount": "$150,000", "status": "Shipped", "date": "2026-03-15"})
    ontology_store.add_entity("E-004", "Order", {"order_number": "ORD-9922", "amount": "$420,000", "status": "Processing", "date": "2026-03-18"})
    ontology_store.add_entity("E-005", "Product", {"sku": "PRD-X1", "name": "Cloud Compute Engine v2", "category": "Software", "unit_price": "$5,000"})
    ontology_store.add_entity("E-006", "Product", {"sku": "PRD-Y2", "name": "AI Analytics Suite", "category": "SaaS", "unit_price": "$12,000"})
    ontology_store.add_entity("E-007", "Facility", {"facility_id": "FAC-DAL", "name": "Dallas Fulfillment Center", "location": "Dallas, TX", "capacity": "500,000 sq ft"})
    ontology_store.add_entity("E-008", "Supplier", {"vendor_id": "SUP-88", "name": "Nvidia Semi Inc", "rating": "4.9/5.0", "status": "Preferred"})

    # Relationships
    ontology_store.add_relationship("E-001", "E-003", "PLACED_ORDER", "R-101", {"channel": "Direct Sales"})
    ontology_store.add_relationship("E-002", "E-004", "PLACED_ORDER", "R-102", {"channel": "Partner Portal"})
    ontology_store.add_relationship("E-003", "E-005", "CONTAINS_PRODUCT", "R-103", {"quantity": 10})
    ontology_store.add_relationship("E-004", "E-006", "CONTAINS_PRODUCT", "R-104", {"quantity": 35})
    ontology_store.add_relationship("E-003", "E-007", "FULFILLED_BY", "R-105", {"shipping_method": "Express Freight"})
    ontology_store.add_relationship("E-007", "E-008", "SUPPLIED_BY", "R-106", {"sla": "99.99%"})

    # Sync graph store
    graph_store.sync_from_ontology(ontology_store)

populate_sample_data()

app = FastAPI(
    title="Enterprise Data Ontology Knowledge Graph API",
    description="Comprehensive enterprise data ontology and knowledge graph REST system and visual dashboard.",
    version="1.0.0"
)

# Pydantic Schemas
class EntityCreate(BaseModel):
    id: str = Field(..., description="Unique entity ID", json_schema_extra={"example": "E-009"})
    type: str = Field(..., description="Entity type e.g., Customer, Order, Product", json_schema_extra={"example": "Customer"})
    properties: Optional[Dict[str, Any]] = Field(default_factory=dict, json_schema_extra={"example": {"name": "Nexus Systems", "tier": "Gold"}})

class EntityUpdate(BaseModel):
    type: Optional[str] = Field(None, json_schema_extra={"example": "Customer"})
    properties: Optional[Dict[str, Any]] = Field(None, json_schema_extra={"example": {"tier": "Platinum"}})

class RelationshipCreate(BaseModel):
    source: str = Field(..., description="Source Entity ID", json_schema_extra={"example": "E-001"})
    target: str = Field(..., description="Target Entity ID", json_schema_extra={"example": "E-003"})
    type: str = Field(..., description="Relationship type", json_schema_extra={"example": "PLACED_ORDER"})
    id: Optional[str] = Field(None, description="Optional custom relationship ID")
    properties: Optional[Dict[str, Any]] = Field(default_factory=dict)

# API Endpoints
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Enterprise Ontology Knowledge Graph API"}

@app.get("/api/v1/entities")
def get_entities(type: Optional[str] = Query(None, description="Filter entities by type")):
    entities = ontology_store.list_entities(entity_type=type)
    return {"count": len(entities), "entities": entities}

@app.post("/api/v1/entities", status_code=status.HTTP_201_CREATED)
def create_entity(payload: EntityCreate):
    entity_dict = payload.model_dump()
    if not validate_entity(entity_dict):
        raise HTTPException(status_code=400, detail="Invalid entity structure")

    created = ontology_store.add_entity(
        entity_id=payload.id,
        entity_type=payload.type,
        properties=payload.properties
    )
    graph_store.sync_from_ontology(ontology_store)
    return {"message": "Entity created successfully", "entity": created}

@app.get("/api/v1/entities/{entity_id}")
def get_entity_by_id(entity_id: str):
    entity = ontology_store.get_entity(entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' not found")

    neighbors = graph_store.get_neighbors(entity_id)
    return {"entity": entity, "neighbors": neighbors}

@app.put("/api/v1/entities/{entity_id}")
def update_entity_by_id(entity_id: str, payload: EntityUpdate):
    updated = ontology_store.update_entity(
        entity_id=entity_id,
        entity_type=payload.type,
        properties=payload.properties
    )
    if not updated:
        raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' not found")

    graph_store.sync_from_ontology(ontology_store)
    return {"message": "Entity updated successfully", "entity": updated}

@app.delete("/api/v1/entities/{entity_id}")
def delete_entity_by_id(entity_id: str):
    deleted = ontology_store.delete_entity(entity_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' not found")

    graph_store.sync_from_ontology(ontology_store)
    return {"message": f"Entity '{entity_id}' deleted successfully"}

@app.get("/api/v1/relationships")
def get_relationships(
    type: Optional[str] = Query(None),
    source: Optional[str] = Query(None),
    target: Optional[str] = Query(None)
):
    relationships = ontology_store.list_relationships(relationship_type=type, source=source, target=target)
    return {"count": len(relationships), "relationships": relationships}

@app.post("/api/v1/relationships", status_code=status.HTTP_201_CREATED)
def create_relationship(payload: RelationshipCreate):
    rel_dict = payload.model_dump()
    if not validate_relationship(rel_dict):
        raise HTTPException(status_code=400, detail="Invalid relationship structure")

    if not ontology_store.get_entity(payload.source):
        raise HTTPException(status_code=400, detail=f"Source entity '{payload.source}' does not exist")
    if not ontology_store.get_entity(payload.target):
        raise HTTPException(status_code=400, detail=f"Target entity '{payload.target}' does not exist")

    created = ontology_store.add_relationship(
        source=payload.source,
        target=payload.target,
        relationship_type=payload.type,
        rel_id=payload.id,
        properties=payload.properties
    )
    graph_store.sync_from_ontology(ontology_store)
    return {"message": "Relationship created successfully", "relationship": created}

@app.get("/api/v1/relationships/{relationship_id}")
def get_relationship_by_id(relationship_id: str):
    rel = ontology_store.get_relationship(relationship_id)
    if not rel:
        raise HTTPException(status_code=404, detail=f"Relationship '{relationship_id}' not found")
    return {"relationship": rel}

@app.delete("/api/v1/relationships/{relationship_id}")
def delete_relationship_by_id(relationship_id: str):
    deleted = ontology_store.delete_relationship(relationship_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Relationship '{relationship_id}' not found")
    graph_store.sync_from_ontology(ontology_store)
    return {"message": f"Relationship '{relationship_id}' deleted successfully"}

@app.get("/api/v1/stats")
def get_graph_stats():
    return graph_store.get_statistics()

# Dashboard Endpoint
@app.get("/", response_class=HTMLResponse)
@app.get("/dashboard", response_class=HTMLResponse)
def render_dashboard():
    stats = graph_store.get_statistics()
    entities = ontology_store.list_entities()
    relationships = ontology_store.list_relationships()

    # Colors for entity types
    type_colors = {
        'Customer': '#3b82f6',
        'Order': '#10b981',
        'Product': '#f59e0b',
        'Facility': '#8b5cf6',
        'Supplier': '#ec4899'
    }

    # Generate HTML cards for entities
    entity_cards_html = ""
    for e in entities:
        color = type_colors.get(e['type'], '#6b7280')
        props_html = "".join([
            f"<div class='prop-row'><span class='prop-key'>{k}:</span> <span class='prop-val'>{v}</span></div>"
            for k, v in e.get('properties', {}).items()
        ])
        entity_cards_html += f"""
        <div class="card entity-card" style="border-left: 4px solid {color};">
            <div class="card-header">
                <span class="badge" style="background: {color}22; color: {color}; border: 1px solid {color}55;">{e['type']}</span>
                <span class="entity-id">{e['id']}</span>
            </div>
            <div class="card-body">
                {props_html}
            </div>
        </div>
        """

    # Generate HTML rows for relationships
    rel_rows_html = ""
    for r in relationships:
        rel_rows_html += f"""
        <tr class="rel-row">
            <td><code class="code-badge">{r.get('id', 'N/A')}</code></td>
            <td><strong style="color: #38bdf8;">{r['source']}</strong></td>
            <td><span class="rel-type-pill">{r['type']}</span></td>
            <td><strong style="color: #34d399;">{r['target']}</strong></td>
            <td><span class="text-muted">{r.get('properties', {})}</span></td>
        </tr>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Enterprise Ontology & Knowledge Graph Dashboard</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg-primary: #0b0f19;
                --bg-secondary: #111827;
                --bg-card: #1f2937;
                --border-color: #374151;
                --text-main: #f9fafb;
                --text-muted: #9ca3af;
                --accent-blue: #38bdf8;
                --accent-emerald: #34d399;
                --accent-purple: #a78bfa;
                --accent-amber: #fbbf24;
            }}
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
                background-color: var(--bg-primary);
                color: var(--text-main);
                line-height: 1.5;
                padding: 24px;
            }}
            .container {{
                max-width: 1400px;
                margin: 0 auto;
            }}
            header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding-bottom: 24px;
                border-bottom: 1px solid var(--border-color);
                margin-bottom: 32px;
            }}
            .logo-title {{
                display: flex;
                align-items: center;
                gap: 16px;
            }}
            .logo-icon {{
                background: linear-gradient(135deg, #0284c7, #6366f1);
                color: white;
                width: 48px;
                height: 48px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 800;
                font-size: 20px;
                box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
            }}
            h1 {{
                font-size: 24px;
                font-weight: 800;
                letter-spacing: -0.02em;
            }}
            .subtitle {{
                color: var(--text-muted);
                font-size: 14px;
            }}
            .status-indicator {{
                display: flex;
                align-items: center;
                gap: 8px;
                background: rgba(16, 185, 129, 0.1);
                border: 1px solid rgba(16, 185, 129, 0.3);
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 13px;
                color: var(--accent-emerald);
                font-weight: 600;
            }}
            .dot {{
                width: 8px;
                height: 8px;
                background-color: var(--accent-emerald);
                border-radius: 50%;
                box-shadow: 0 0 8px var(--accent-emerald);
            }}
            /* Stats Grid */
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-bottom: 32px;
            }}
            .stat-card {{
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                border-radius: 14px;
                padding: 20px;
                transition: transform 0.2s;
            }}
            .stat-card:hover {{
                transform: translateY(-2px);
                border-color: var(--accent-blue);
            }}
            .stat-label {{
                font-size: 13px;
                color: var(--text-muted);
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}
            .stat-value {{
                font-size: 32px;
                font-weight: 800;
                margin-top: 8px;
                color: var(--accent-blue);
                font-family: 'JetBrains Mono', monospace;
            }}
            /* Dashboard Sections */
            .section-title {{
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 16px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .section-grid {{
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 24px;
                margin-bottom: 32px;
            }}
            @media (max-width: 1024px) {{
                .section-grid {{ grid-template-columns: 1fr; }}
            }}
            .panel {{
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                border-radius: 16px;
                padding: 24px;
            }}
            /* Entity Cards Grid */
            .entity-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                gap: 16px;
                margin-top: 16px;
            }}
            .entity-card {{
                background: var(--bg-card);
                border-radius: 12px;
                padding: 16px;
                border: 1px solid var(--border-color);
            }}
            .card-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;
            }}
            .badge {{
                font-size: 11px;
                font-weight: 700;
                padding: 2px 8px;
                border-radius: 6px;
                text-transform: uppercase;
            }}
            .entity-id {{
                font-family: 'JetBrains Mono', monospace;
                font-size: 13px;
                color: var(--text-muted);
            }}
            .prop-row {{
                font-size: 13px;
                margin-bottom: 4px;
                display: flex;
                justify-content: space-between;
            }}
            .prop-key {{
                color: var(--text-muted);
            }}
            .prop-val {{
                font-weight: 600;
                color: var(--text-main);
            }}
            /* Relationships Table */
            .rel-table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 16px;
                font-size: 14px;
            }}
            .rel-table th {{
                text-align: left;
                padding: 12px;
                color: var(--text-muted);
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                border-bottom: 1px solid var(--border-color);
            }}
            .rel-table td {{
                padding: 12px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }}
            .code-badge {{
                font-family: 'JetBrains Mono', monospace;
                background: rgba(255, 255, 255, 0.05);
                padding: 2px 6px;
                border-radius: 4px;
                font-size: 12px;
            }}
            .rel-type-pill {{
                background: rgba(56, 189, 248, 0.1);
                color: var(--accent-blue);
                border: 1px solid rgba(56, 189, 248, 0.2);
                padding: 3px 10px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 700;
            }}
            /* Graph Visual Preview */
            .graph-canvas-mock {{
                height: 280px;
                background: radial-gradient(circle, #1e293b 1px, transparent 1px);
                background-size: 20px 20px;
                background-color: #0f172a;
                border-radius: 12px;
                border: 1px dashed var(--border-color);
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow: hidden;
            }}
            .graph-node {{
                position: absolute;
                padding: 8px 14px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 700;
                box-shadow: 0 4px 12px rgba(0,0,0,0.5);
                border: 2px solid;
            }}
            .node-1 {{ top: 30px; left: 40px; background: #1e3a8a; border-color: #3b82f6; color: #93c5fd; }}
            .node-2 {{ top: 180px; left: 120px; background: #064e3b; border-color: #10b981; color: #a7f3d0; }}
            .node-3 {{ top: 90px; left: 240px; background: #78350f; border-color: #f59e0b; color: #fde68a; }}
            .node-4 {{ top: 200px; right: 60px; background: #4c1d95; border-color: #8b5cf6; color: #ddd6fe; }}
            .node-5 {{ top: 40px; right: 100px; background: #831843; border-color: #ec4899; color: #fbcfe8; }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <div class="logo-title">
                    <div class="logo-icon">KG</div>
                    <div>
                        <h1>Enterprise Data Ontology & Knowledge Graph</h1>
                        <div class="subtitle">Real-time Entity Analytics, Schema Mapper, and Graph Visualizer</div>
                    </div>
                </div>
                <div class="status-indicator">
                    <div class="dot"></div>
                    System Active & Synchronized
                </div>
            </header>

            <!-- Metrics -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-label">Total Entities</div>
                    <div class="stat-value">{stats['total_nodes']}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Total Relationships</div>
                    <div class="stat-value" style="color: var(--accent-emerald);">{stats['total_edges']}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Average Node Degree</div>
                    <div class="stat-value" style="color: var(--accent-purple);">{stats['average_degree']}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Entity Classes</div>
                    <div class="stat-value" style="color: var(--accent-amber);">{len(stats['node_type_counts'])}</div>
                </div>
            </div>

            <!-- Top Panel: Graph Topology Visualizer Preview & Breakdown -->
            <div class="section-grid">
                <div class="panel">
                    <div class="section-title">
                        <span>🕸️ Knowledge Graph Topology</span>
                    </div>
                    <div class="graph-canvas-mock">
                        <div class="graph-node node-1">Customer (Acme)</div>
                        <div class="graph-node node-2">Order (ORD-9921)</div>
                        <div class="graph-node node-3">Product (Compute v2)</div>
                        <div class="graph-node node-4">Facility (Dallas)</div>
                        <div class="graph-node node-5">Supplier (Nvidia)</div>
                        <svg style="position: absolute; width: 100%; height: 100%; pointer-events: none;">
                            <line x1="120" y1="50" x2="160" y2="190" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4" />
                            <line x1="200" y1="200" x2="260" y2="120" stroke="#10b981" stroke-width="2" />
                            <line x1="220" y1="200" x2="320" y2="210" stroke="#8b5cf6" stroke-width="2" />
                            <line x1="390" y1="200" x2="380" y2="70" stroke="#ec4899" stroke-width="2" stroke-dasharray="4" />
                        </svg>
                    </div>
                </div>
                <div class="panel">
                    <div class="section-title">📊 Ontology Distribution</div>
                    <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 16px;">
                        {"".join([
                            f"<div style='display:flex; justify-content:space-between; align-items:center; background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px;'><span style='font-weight:600;'>{ntype}</span><span class='code-badge'>{count} nodes</span></div>"
                            for ntype, count in stats['node_type_counts'].items()
                        ])}
                    </div>
                </div>
            </div>

            <!-- Entities Panel -->
            <div class="panel" style="margin-bottom: 32px;">
                <div class="section-title">🏢 Managed Entities</div>
                <div class="entity-grid">
                    {entity_cards_html}
                </div>
            </div>

            <!-- Relationships Panel -->
            <div class="panel">
                <div class="section-title">🔗 Enterprise Relationships</div>
                <table class="rel-table">
                    <thead>
                        <tr>
                            <th>Rel ID</th>
                            <th>Source Entity</th>
                            <th>Relationship Type</th>
                            <th>Target Entity</th>
                            <th>Properties</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rel_rows_html}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
