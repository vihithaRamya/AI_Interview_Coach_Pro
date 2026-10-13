def evaluate_answer(question, answer):

    answer = answer.lower()

    score = 50

    feedback = []


    # Check answer length
    if len(answer.split()) >= 20:
        score += 10
    else:
        feedback.append(
            "Try to give a more detailed explanation."
        )


    # Check relevance keywords

    keywords = {
        "tell me about yourself":
        [
            "education",
            "skills",
            "project",
            "experience"
        ],

        "why should we hire you":
        [
            "skills",
            "knowledge",
            "contribute",
            "team"
        ],

        "strengths and weaknesses":
        [
            "strength",
            "improve",
            "learning"
        ],

        "project":
        [
            "technology",
            "implementation",
            "result"
        ]
    }


    for key, words in keywords.items():

        if key in question.lower():

            matches = 0

            for word in words:

                if word in answer:
                    matches += 1


            score += matches * 5


            if matches == 0:

                feedback.append(
                    "Answer does not fully address the question."
                )


    # Grammar/basic communication

    if answer.endswith("."):

        score += 5

    else:

        feedback.append(
            "Use complete sentences."
        )


    # Limit score

    if score > 100:

        score = 100


    if score < 0:

        score = 0



    # Hiring prediction

    if score >= 80:

        status = "High Chance"

    elif score >= 60:

        status = "Average Chance"

    else:

        status = "Needs Improvement"



    return {

        "overall": score,

        "communication": min(score + 5,100),

        "technical": score,

        "confidence": min(score + 3,100),

        "grammar": min(score + 7,100),

        "status": status,

        "feedback": feedback

    }