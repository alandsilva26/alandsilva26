languages = [
    {
        "message": "Dart",
        "color": "00B4AB",
        "logo": "dart",
        "logoColor": "0175C2",
    },
    {
        "message": "HTML",
        "color": "e44b23",
        "logo": "HTML5",
        "logoColor": "E34F26",
    },
    {
        "message": "JavaScript",
        "color": "f1e05a",
        "logo": "JavaScript",
        "logoColor": "F7DF1E",
    }, {
        "message": "PHP",
        "color": "4F5D95",
        "logo": "PHP",
        "logoColor": "777BB4",
    }, {
        "message": "CSS",
        "color": "563d7c",
        "logo": "CSS3",
        "logoColor": "1572B6",
    }, {
        "message": "Java",
        "color": "b07219",
        "logo": "Java",
        "logoColor": "007396",
    }, {
        "message": "Python",
        "color": "3572A5",
        "logo": "Python",
        "logoColor": "3776AB",
    },
    {
        "message": "C",
        "color": "555555",
        "logo": "C",
        "logoColor": "A8B9CC",
    },
]

finalString = ""
for lang in languages:
    # template = "![{name}](https://img.shields.io/static/v1?style=flat&label=%20&labelColor=%23555&logo={logo}&logoColor=%23{logoColor}&message={message}&color=%23{color})".format(
    #     name=lang["message"], logo=lang["logo"], logoColor=lang["logoColor"], message=lang["message"], color=lang["color"])
    template = "![{name}](https://img.shields.io/static/v1?style=flat&label=&message={message}&color=%23{color})".format(
        name=lang["message"],  message=lang["message"], color=lang["color"])

    finalString += template.strip() + " "

print(finalString)
