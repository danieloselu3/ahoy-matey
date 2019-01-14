class Ship:
    def __init__(self, draft, crew): #initialize class with crew and draft
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
     #find the total drag of loot by taking away draft by crew from total draft
        booty_onboard = self.draft - self.crew*1.5 #
        if booty_onboard <= 20:
            #return True only if the draft is greater than 20
            return False
        else:
            return True
