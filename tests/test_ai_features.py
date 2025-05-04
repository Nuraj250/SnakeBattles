def test_ai_chat_response_format():
    """Test if AI chatbot returns text"""
    from app.ai.chat import chat_with_ai
    reply = chat_with_ai("Hello")
    assert isinstance(reply, str)
    assert len(reply) > 0
