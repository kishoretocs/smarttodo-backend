from .openrounter_client import query_openrouter

def generate_task_suggestion(task_data, context_data):
    task_prompt = f"""
    You are a smart task assistant. Based on the following:

    Task:
    Title: {task_data.get('title')}
    Description: {task_data.get('description')}

    Context:
    {context_data}

    Respond in JSON with:
    {{
        "priority_score": float (1-10),
        "suggested_deadline": string (e.g., "2025-07-10T14:00:00"),
        "suggested_category": string,
        "enhanced_description": string,
        "tags": list of strings
    }}
    """

    ai_response = query_openrouter(task_prompt)
    try:
        # Optional: use `json.loads(ai_response)` if response is strict JSON
        import ast
        return ast.literal_eval(ai_response)
    except Exception:
        return {"error": "AI response could not be parsed"}
