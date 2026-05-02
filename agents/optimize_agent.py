from core.llm_client import get_client
def run(code):
    client = get_client()
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":f"优化代码：{code}"}]
    )
    return r.choices[0].message.content
