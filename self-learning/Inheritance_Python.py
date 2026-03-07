class TeamMember:
    def __init__(self,name,teamName,expInYears):
        self.name=name
        self.teamName = teamName
        self.expInYears = expInYears
        self.projects=[]


    def  averageSalary(self):
        return (int(self.expInYears) * 100)/ 12



class DevMember(TeamMember):
    def __init__(self,name,teamName,expInYears,skills):
        super().__init__(name,teamName,expInYears)
        self.skills = skills

    def devSkills(self):
        return f"Set of skills of Dev Member {self.name} with {self.skills}"


class QAMember(TeamMember):
    def __init__(self,name,teamName,expInYears,tools):
        super().__init__(name,teamName,expInYears)
        self.tools = tools




dev1 = DevMember("Praneeth","JPMC","11",'''Java,AWS,Python,SprintBoot''')

print(DevMember.averageSalary(dev1))
print(DevMember.devSkills(dev1))

