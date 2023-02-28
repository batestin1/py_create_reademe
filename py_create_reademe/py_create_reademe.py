def create_readme():
     # create a readme.md file
     file = open("readme.md", "w")

     var_title = input("Project name: ").replace(" ", "%20").upper()
     var_user = input("Your name: ").replace(" ", "%20").upper()

     first_line = f"# {var_title.replace('%20', ' ')}"
     header = f"""<img src="https://img.shields.io/static/v1?label={var_title}&message={var_user}&color=7159c1&style=flat-square&logo=ghost" />"""

     # text input for project description
     print("Describe your project:")
     print("Type 'exit' on a separate line to end text entry.\n")
     description=""
     while True:
         line = input()
         if line.strip().lower() == "exit":
             break
         description += line + "\n"

     # text input for the "How to install" section
     print("How to install the project:")
     print("Type 'exit' on a separate line to end text entry.\n")
     how_to_install=""
     while True:
         line = input()
         if line.strip().lower() == "exit":
             break
         how_to_install += line + "\n"

     # text input for the "How it works" section
     print("How the project works:")
     print("Type 'exit' on a separate line to end text entry.\n")
     how_it_works=""
     while True:
         line = input()
         if line.strip().lower() == "exit":
             break
         how_it_works += line + "\n"

     # write the contents in the readme.md file
     file.write(f"{first_line}\n\n")
     file.write(f"{header}\n\n")
     file.write(f"## Description\n\n{description}\n\n")
     file.write(f"## How to install\n\n```\n{how_to_install}\n```\n\n")
     file.write(f"## How it works\n\n```\n{how_it_works}\n```\n\n")

     # close the readme.md file
     file.close()

     print("The README.md file was successfully created!")