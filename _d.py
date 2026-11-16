def d(slug, name, cat, scope, ladder, projects, tools, practice, safety=""):
    """One discipline. `ladder` and `projects` are '|' separated strings."""
    return {
        "slug": slug,
        "name": name,
        "category": cat,
        "scope": scope,
        "ladder": [x.strip() for x in ladder.split("|")],
        "projects": [x.strip() for x in projects.split("|")],
        "tools": tools,
        "practice": practice,
        "safety": safety,
    }
