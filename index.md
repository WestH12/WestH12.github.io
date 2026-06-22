---
layout: default
title: CS 499 - Computer Science Capstone ePortfolio
---

# Computer Science Professional ePortfolio
**Course:** CS 499 - Computer Science Capstone  
**Developer:** Westley Hunter  
**Date:** June, 2026

---

## 📑 Professional Self-Assessment

### Introduction & Professional Value
> My name is Westley Hunter, and I am a senior in SNHU's Computer Science Bachelor of Science program. Throughout my academic journey, I have embarked on personal side projects, YouTube rabbit holes of interesting topics, and desire to practice machine learning. My coursework has allowed me to confidently compete in Kaggle competitions and incorporate learned topics into functional applications. I am grateful for my time at SNHU and hope to gain a job in the machine learning field.
> 
> Developing and completing this portfolio is a great final achievement in the computer science journey here at SNHU. Bringing together these 3 artifacts helped me to highlight my strengths of familiarity across many different technical domains, a passion to learn and build side projects, and pushing through uncertain territory. Throughout my coursework, I have learned about foundational machine learning topics, how to identify, clean, and utilize data sources and honed a skill to craft environment specific algorithms. For example, when creating my Wordle Bot, I had to combine information theory with programming principles to identify the best first guess by looking ahead. Additionally, initial full testing runs took around 15 hours but with the innovative approach of precomputing the answers with a lookup table dropped the time to around 7 minutes. Throughout my coursework, I have had the opportunity to develop a data integrity plan, propose and evaluate a machine learning model for a selected problem, and employ linear algebra to solve real-world problems. Overall, these topics and experiences have placed me in a great position to become a machine learning engineer.
>
> The artifacts for this project are a full-stack web application built with the MEAN stack, a Wordle Bot incorporating word frequencies, and a MongoDB middleware that performs aggregations on the server-side. All the artifacts showcase my ability to build end-to-end applications, construct dynamic and optimized algorithms, and manage the balance of the client-server environment. 

### Core Competency Reflections
* **Collaborating in a Team Environment:** Participated in numerous discussions posts to discuss current technical problems, different algorithmic approaches
* **Communicating with Stakeholders:** Developed multiple documents to communicate technical topics and approaches to nontechnical stakeholders through precise and clean communication.
* **Data Structures and Algorithms:** Navigated complex problems through dynamic and systematic programming while utilizing the appropriate data structures to balance computational demands and design parameters.
* **Software Engineering & Databases:** Manufactured full-stack applications that managed front-end rendering and server-side logic within popular tech stacks and optimized client-server connections.
* **Security Mindset:** Created security-minded applications through input sanitization, vulnerability scanning, implementing secure design patterns, and anonymization of data. 

---

## 🎥 Code Review
* **Video Delivery:** https://youtu.be/svvfcTDH0GQ  


---

## 🚀 Artifact Enhancements & Narratives

### 📂 Enhancement 1: Software Design and Engineering - Full Stack Website with MEAN stack
* **Original Codebase:** https://github.com/WestH12/WestH12.github.io/tree/main/travlr_Original
* **Enhanced Codebase:** https://github.com/WestH12/WestH12.github.io/tree/main/travlr_Enhanced

#### Reflection Narrative
The artifact I selected for the first category of software design and engineering for CS499 is a full-stack application I created for CS465: Full Stack Development I. The full-stack website is built using the MEAN stack (MongoDB, Express, Angular, and Node.js). It is a travel website for the company Travlr that shows trips, meals, and other pertinent information while giving administration a backend portal to create, edit, and delete website information with a secure login interface. The application was created around 2 months ago. 

The Travlr website was included within the ePortofilio due to it exemplifying the complete software design and engineering lifecycle. Websites are what fuel the modern technological world across the world wide web.   Thus, full-stack websites are a common cornerstone within portfolios and are solid earmarks of an experienced developer. A specific component that highlights my skills in software development is the integration of a database into the architecture to be displayed on the website and allow for basic CRUD capabilities in a user-friendly backend environment. Additionally, using the MEAN technology stack is a great exemplification of my software development abilities as it shows I am able to learn, implement, and debug modern tech stacks. The artifact was improved by integrating comprehensive API functionality to ensure that all routes and API calls work before deployment. Additionally, it ensures that the login is a secure process, and CRUD functionality requires a JWT token to modify the database. 

I completely fulfilled the course outcomes that I sought to satisfy with this enhancement. By creating a comprehensive API testing framework for the application, I improved upon the overall security of the application. All future developments can easily ensure that all APIs are secure, and the login process is executing as intended. I think an additional course outcome that I satisfied with this enhancement is outcome 4 as I used an industry standard testing framework. By employing Jest and Supertest, I demonstrated the ability to use well-founded techniques and tools to increase the value of the product. 

Developing the enhancement for this category was very difficult initially as I was learning the testing library, navigating the project architecture, and integrating the new technology within the existing application. Some initial problems were requests improperly created that were returning null data and implementing the JWT token within the edit and delete test functions. 


---

### 📂 Enhancement 2: Algorithms and Data Structures - Wordle Bot
* **Original Codebase:** https://github.com/WestH12/WestH12.github.io/tree/main/Wordle%20Bot_Original/Wordle%20Bot
* **Enhanced Codebase:** https://github.com/WestH12/WestH12.github.io/tree/main/Wordle%20Bot_Enhanced

#### Reflection Narrative
The artifact I choose for the category of algorithms and data structures is a Wordle bot I created in my free time. While the popularity peak of Wordle (Wordle — The New York Times) has long since passed, I was inspired to create this project by 3Blue1Brown’s development of his own Wordle bot (Solving Wordle using information theory). By using information theory, entropy, information gain, and word frequency, my bot systematically narrows down the guess list to the answer while using explorer and sacrifice guesses to achieve the best score possible. Over the past month and a half, I have been working on this bot in my free time and its inclusion in this course has allowed for more time to be devoted to it. As of current submittal, the bot is on its fourth version as it has progressed through initial functionality, explorer and sacrifice guess implementation, and evaluation optimizations. 

I included this artifact in my ePortfolio because of its great exemplification of different self-created algorithms and employment of various data structures. Within this project, the bot relies on the preestablished entropy formula, a regular and explorer feedback algorithm, a regular and sacrifice guess evaluation algorithm, and weighing all the word frequencies to create frequencies within the context of the guess list. The bot uses all different data structures like lists, Pandas DataFrames and Series, JSON and CSV files, sets, and dictionaries. A crucial data structures for the bot is the explorer_lookup dictionary used on the second turn to rapidly lookup the pre-calculated best word based on the provided feedback. With the rapid read speed of the dictionary, the bot gets to skip the largest computational demand as the average guess list is still 716 words long; which requires significant computing power. While this may seem trivial in single uses of the bot, this computation bloats the full testing time of 14,000+ words to just over 15 hours. Additionally, the bot missed 1,731 words with an average score of 4.85. The initial plan to enhance this artifact included using the known answer list and providing a notable boost to known answers in the evaluation function. However, that idea was substituted for adding a second turn explorer guess and a sacrifice guess function in the fourth and fifth turns. 
The second turn explorer guess aims to rapidly provide the best second turn guess based on the provided feedback. The guess is evaluated against a criterion that selects the word with the highest information gain that does not included eliminated letters from the first turn. This differs from the regular evaluation function as the explorer guess takes the guess list, removes words with the eliminated words but does not narrow it down further based on letters identified to be in their correct position. This subtle modification allows the bot to prioritize gaining knowledge on unknown letters without restricting itself to a smaller word list. Additionally, using a precalculated dictionary lookup significantly accelerates the bot’s performance and lowers the testing time across 14,000+ words to 7.31 minutes with 1, 262 misses and an average score of 4.81.
	The second enhancement implemented a function to determine if the bot is stuck in a trap where multiple letter positions are known but there are numerous similar remaining guesses. For example, the bot knows the word has the last 4 letters of _IGHT but there a numerous guesses like FIGHT, MIGHT, LIGHT, NIGHT, RIGHT, or TIGHT. However, the bot does not have 6 turns left to slowly eliminate each word. Therefore, the bot identifies the trap by looking at length of guess list at turn four and five and then looks for any word in the 14,000+ master word list and picks the word that contains the most remaining unknown letters. Hopefully, this method identifies the trap and radically reduces the remaining guest list by submitting a sacrificial word. By implementing this trap detection, the testing time rose by .11 minutes but missed words dropped to 314 words with an average score of 4.56.
While not a performance update, the testing function takes the each secret word, the remaining amount of words after each turn, and the win status of the word and writes it to a CSV for a more detailed analysis. 

I set out to satisfy the course outcomes of building a collaborative environment and design and evaluate computing solutions to solve a given problem. I satisfied the first course outcome by documenting my development, testing, and analysis of my project in the GitHub. By doing all of this in an open environment, new or experienced developers can examine the steps I took within the project and its overall impact on the bot’s performance. Additionally, I believe that I satisfied the third course outcome by designing, implementing, and evaluating the different algorithms within my artifact. Each new addition to my bot was evaluated through a complete testing run and while some additions raised the total testing time, the number of missed words and average score dropped dramatically; thus, making the additions worthwhile. 

The enhancement process for this artifact included a substantial amount of time and numerous testing iterations. By creating and improving this artifact, I learned a lot about information theory, how to weigh items in evaluation functions, and optimizing performance. A significant challenge I faced was implementing the sacrifice word function to mitigate word traps. I had difficulty determining the algorithmic approach to find and prioritize words with unused letters. However, I was able to discern how to prioritize words that would reduce the guess list by around half. Another challenge I faced was loading in the explorer lookup csv correctly and reformatting it to the desired shape so I could easily index the best word upon given feedback. 


---

### 📂 Enhancement 3: Databases - MongoDB Animal Shelter Aggregations  
* **Original Codebase:** https://github.com/WestH12/WestH12.github.io/tree/main/Animal_Shelter_Original
* **Enhanced Codebase:** https://github.com/WestH12/WestH12.github.io/tree/main/Animal_Shelter_Enhanced

#### Reflection Narrative
The artifact I chose for the category of databases is a PyMongo middleware application for an animal shelter that handles intake and adoption services for animals in the Austin area. I created the middleware application to connection to a MongoDB instance for the class of CS340.

I included this artifact within my ePortfolio because it represents a real-world system which could host numerous amounts of information. Additionally, MongoDB is a very common database used across the industry and a great way to highlight industry needed skills. To improve this artifact, I implemented aggregation and statistical analysis of the database on the server-side and completely mitigated the client from having to sacrifice computational power. By adding three different functions with hardcoded specific pipelines, the computation and pipeline specification are abstracted away from the user. The three functions provide analytics on each animal type, highlight high dog breed volumes in the kennel, and tactical metrics on animals rescued. 

I did satisfy the fourth course outcome of using well-founded and innovative techniques, skills, and tools to deliver value and meet industry standards. By moving the computational load to the server, the client and their computers are free to allocate their resources to other areas. Additionally, the server-side of most environments tend to have more computational power and thus allows for a uniform processing time. I feel that the artifact’s development expanded to cover the fifth outcome related to a security mindset and mitigation of potential exploits. By hardcoding each pipeline into their own function, functions return the same thing each time and prevent wayward pipelines from being passed to the database. 

The process of enhancing the artifact was initially difficult as I had to familiarize myself with the language and syntax within MongoDB. However, afterwards, I made my way through constructing effective pipelines by continuously trying different approaches. Through this developmental process, I learned how stages and pipelines work in MongoDB as well as executing aggregations from the pymongo level. 


---

