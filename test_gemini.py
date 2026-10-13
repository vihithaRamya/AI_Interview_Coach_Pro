from backend.gemini_ai import generate_ideal_answer


answer = generate_ideal_answer(
    "Explain Java OOP concepts"
)


print(answer)