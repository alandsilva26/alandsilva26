import random

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

frameworks = [{
    "message": "Flutter",
}, {
    "message": "React",
}, {
    "message": "Django",
}, {
    "message": "Sass",
}, {
    "message": "Bootstrap",
}, {
    "message": "Jquery",
},
]

Tools = [{
    "message": "Docker",
}, {
    "message": "Git",
}, {
    "message": "Github Actions",
}, {
    "message": "Firebase",
},
]

colors = ["brightgreen", "red", "%23563d7c",
          "orange", "%23555555" "green", "blue", "blueviolet", ]


# Main
if __name__ == "__main__":
    initColor = random.randint(0, len(colors) - 1)
    finalString = ""

    # menu
    choice = 1

    try:
        choice = int(
            input("1. itemuages\n2. Frameworks\n3.Tools\nEnter your choice(Default 1): "))
    except:
        print("No value entered")

    itemList = None

    if(choice == 1):
        itemList = languages
    elif (choice == 2):
        itemList = frameworks
    elif(choice == 3):
        itemList = Tools
    else:
        print("Invalid choice")

    if itemList != None:
        for item in itemList:
            color = colors[initColor]
            initColor = (initColor + 1) % len(colors)
            print(initColor)
            if "color" in item:
                color = "%23{}".format(item["color"])
            message = item["message"].replace(" ", "%20")
            # template = "![{name}](https://img.shields.io/static/v1?style=flat&label=%20&labelColor=%23555&logo={logo}&logoColor=%23{logoColor}&message={message}&color=%23{color})".format(
            #     name=item["message"], logo=item["logo"], logoColor=item["logoColor"], message=item["message"], color=item["color"])
            template = "![{name}](https://img.shields.io/static/v1?style=flat&label=&message={message}&color={color})".format(
                name=message,  message=message, color=color)

            finalString += template.strip() + " "

        print(finalString)
