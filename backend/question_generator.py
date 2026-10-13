def generate_questions(skills):

    questions = []


    hr_questions = [

        "Tell me about yourself.",

        "Why should we hire you?",

        "What are your strengths and weaknesses?",

        "Explain your final year project."

    ]


    questions.extend(hr_questions)



    skill_questions = {


        "python":[

            "Explain Python OOP concepts.",

            "Difference between list and tuple.",

            "Explain exception handling in Python."

        ],


        "sql":[

            "Explain SQL joins.",

            "Difference between WHERE and HAVING.",

            "What is normalization?"

        ],


        "machine learning":[

            "Difference between AI and Machine Learning.",

            "Explain supervised and unsupervised learning.",

            "What is overfitting?"

        ],


        "django":[

            "Explain Django architecture.",

            "What are models and views in Django?"

        ],


        "java":[

            "Explain Java OOP concepts.",

            "Difference between JDK and JRE."

        ]

    }



    for skill in skills:

        skill = skill.lower()


        if skill in skill_questions:

            questions.extend(
                skill_questions[skill]
            )


    return questions[:15]