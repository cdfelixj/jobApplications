def coverLetter(company_name, role):
    output = f"""Dear {company_name} Team,

I am currently studying at Hong Kong Baptist University, majoring in Business Computing & Data Analytics, from which I will be graduating in May 2026. It is with great interest that I am applying for the {role} position at {company_name}.

I am confident that my technical qualifications and work experiences developing solutions for clients and end users make me an excellent candidate for this internship. I would appreciate the opportunity to discuss how I can help support {company_name}'s needs.

Thank you for your consideration.
Attached you will find my CV and recommendation letters.

Yours sincerely,
Juan Felix Pangestu
"""
    return output



with open('cover_letter.txt', 'w') as f:
    f.write(coverLetter('FansWifi', 'Web Application Developer Intern'))