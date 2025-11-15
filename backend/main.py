from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
import json
from pathlib import Path

app = FastAPI(title="Candidate Management API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", 'https://thetasoftware.vercel.app'],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load mock data
# Try multiple paths for compatibility with local and deployed environments
def get_data_file_path():
    """Get the path to the candidates.json file, trying multiple locations"""
    possible_paths = [
        Path(__file__).parent / "mock-data" / "candidates.json",  # Backend directory (for deployment)
        Path(__file__).parent.parent / "mock-data" / "candidates.json",  # Root directory (for local dev)
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    raise FileNotFoundError(f"Could not find candidates.json in any of these locations: {[str(p) for p in possible_paths]}")

def load_candidates():
    """Load candidates from JSON file"""
    data_file = get_data_file_path()
    with open(data_file, "r") as f:
        data = json.load(f)
    return data["candidates"]


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Candidate Management API", "docs": "/docs"}


@app.get("/api/candidates")
def get_candidates(
    search: Optional[str] = Query(None, description="Search by name, position, or company"),
    application_type: Optional[List[str]] = Query(None, description="Filter by application type (active, archived)"),
    job_id: Optional[List[str]] = Query(None, description="Filter by job ID"),
    source: Optional[List[str]] = Query(None, description="Filter by source"),
    has_availability: Optional[bool] = Query(None, description="Filter by availability"),
    has_interviews: Optional[bool] = Query(None, description="Filter by interviews"),
    full_text_search: Optional[bool] = Query(False, description="Enable full text search (includes resumes and notes)"),
    sort: Optional[str] = Query("activity_desc", description="Sort option: activity_desc, activity_asc, name_asc, name_desc"),
):
    """
    Get filtered candidates

    Returns all matching candidates
    """

    # Step 1: Load all candidates
    candidates = load_candidates()

    # Step 2: Filter by search term (if provided)
    # TODO: Implement search filtering here
    # HINT: Check if 'search' exists, then filter candidates where search term
    # appears in name, position, or company (case-insensitive)
    #
    # Example pseudocode:
    # if search:
    #     search_lower = search.lower()
    #     candidates = [c for c in candidates
    #                   if search_lower in c['name'].lower() or
    #                      search_lower in c['position'].lower() or
    #                      search_lower in c['company'].lower()]

    # Filter by search term
    filtered_candidates = candidates
    if search:
        search_lower = search.lower()
        if full_text_search:
            # Full text search: search in name, position, company, job_title, status, action_link, and source
            filtered_candidates = [
                c for c in candidates
                if search_lower in c.get('name', '').lower() or
                   search_lower in c.get('position', '').lower() or
                   search_lower in c.get('company', '').lower() or
                   search_lower in c.get('job_title', '').lower() or
                   search_lower in c.get('status', '').lower() or
                   search_lower in c.get('action_link', '').lower() or
                   search_lower in c.get('source', '').lower()
            ]
        else:
            # Standard search: only name, position, and company
            filtered_candidates = [
                c for c in candidates
                if search_lower in c.get('name', '').lower() or
                   search_lower in c.get('position', '').lower() or
                   search_lower in c.get('company', '').lower()
            ]

    if application_type:
        # Filter by application_type (active, archived)
        filtered_candidates = [
            c for c in filtered_candidates
            if c.get('application_type') in application_type
        ]

    if job_id:
        # Filter by job_id
        filtered_candidates = [
            c for c in filtered_candidates
            if c.get('job_id') in job_id
        ]

    if source:
        # Filter by source
        filtered_candidates = [
            c for c in filtered_candidates
            if c.get('source') in source
        ]

    if has_availability is not None:
        # Filter by availability: True or False
        filtered_candidates = [
            c for c in filtered_candidates
            if c.get('has_availability') == bool(has_availability)
        ]

    if has_interviews is not None:
        # Filter by whether candidate has interviews
        filtered_candidates = [
            c for c in filtered_candidates
            if c.get('has_interviews') == bool(has_interviews)
        ]

    # Sort candidates
    if sort == 'activity_desc':
        filtered_candidates = sorted(
            filtered_candidates,
            key=lambda x: x.get('last_activity', ''),
            reverse=True
        )
    elif sort == 'activity_asc':
        filtered_candidates = sorted(
            filtered_candidates,
            key=lambda x: x.get('last_activity', '')
        )
    elif sort == 'name_asc':
        filtered_candidates = sorted(
            filtered_candidates,
            key=lambda x: x.get('name', '').lower()
        )
    elif sort == 'name_desc':
        filtered_candidates = sorted(
            filtered_candidates,
            key=lambda x: x.get('name', '').lower(),
            reverse=True
        )

    total = len(filtered_candidates)

    return {
        "candidates": filtered_candidates,
        "total": total
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
