from datetime import datetime

def coverLetter(company_name, role, industry):
    current_date = datetime.now().strftime("%B %d, %Y")
    output = f"""{current_date}
{company_name}

To Whom it May Concern,

I am writing to express my enthusiastic interest in the {role} position at {company_name}. As a third-year student majoring in Business Computing & Data Analytics at Hong Kong Baptist University, I have developed a robust foundation in both software development and finance, and I am eager to leverage these skills within {company_name}'s dynamic environment. Your commitment to innovation and leadership in the {industry} industry is particularly inspiring, and I am drawn to your dedication to using technology to drive financial solutions. The opportunity to work with your extensive resources and industry expertise aligns perfectly with my passion.

My recent experience as a Software Engineer Intern at Wizpresso has been pivotal in enhancing my understanding of software engineering and its application in financial technology. Over the summer, I was responsible for refactoring the user management portal, where I developed 15 new features and optimized 10 existing ones to improve portal speed and user engagement. This role underscored the critical importance of delivering fast, reliable, and intuitive software in financial services, where every millisecond can impact trading and user satisfaction. Additionally, I refactored the user management system to enhance efficiency and scalability, skills that are crucial for handling large datasets and complex transactions in a tech-driven institution like {company_name}. Working directly with sensitive financial data from various companies, I routed APIs to dynamically display data to applications addressing stringent requirements around security, reliability and responsiveness within regulated financial markets, enabling our data science team to manage information accurately.

At Admazes, I had the opportunity to contribute significantly as a Software Engineer Intern. During my tenure, I worked on developing and enhancing a Local Large Language Model using LangChain. This project allowed me to improve the model's response accuracy by 25% through better semantic understanding and advanced search capabilities. Additionally, I analyzed datasets using BigQuery, optimizing data retrieval efficiency by 30%. By crafting and executing over 100 complex SQL queries, I was able to generate actionable insights that led to a 20% boost in operational efficiency. This experience reinforced the importance of precise and efficient data processing—skills that are vital in the {industry} world. The {role} position aligns perfectly with my aspiration to merge technology with finance. The prospect of collaborating with passionate individuals from diverse backgrounds, including fellow {industry} enthusiasts and experts from {company_name}, is incredibly motivating. I am excited about the chance to exchange ideas and skills and contribute to projects that can create a lasting positive impact. I am confident that my technical skills, combined with my enthusiasm for innovation and teamwork, make me a strong candidate for the {role} position.

Thank you for considering my application. I look forward to the possibility of contributing to {company_name} and making a meaningful difference through technology.

"""
    return output


def emailLetter(company_name, role):
    output = f"""Dear {company_name} Team,

I am currently studying at Hong Kong Baptist University, majoring in Business Computing & Data Analytics, from which I will be graduating in May 2026. It is with great interest that I am applying for the {role} position at {company_name}.

I am confident that my technical qualifications and work experiences developing solutions for clients and end users make me an excellent candidate for this internship. I would appreciate the opportunity to discuss how I can help support {company_name}'s needs.

Thank you for your consideration.
Attached you will find my CV and recommendation letters.

Yours sincerely,
Juan Felix Pangestu
"""
    return output

company = 'DXC Technology'
position = 'Java Intern'
industry = 'technology'




with open('email.txt', 'w') as f:
    f.write(emailLetter(company, position))

with open('cover_Letter.txt', 'w', encoding='utf-8') as f:
    f.write(coverLetter(company, position, industry))