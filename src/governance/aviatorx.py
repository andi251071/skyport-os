# AVIATOR-X: AI Governance Engine for Skyport OS

class Proposal:
    def __init__(self, title: str, description: str, proposer: str):
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = {"yes": 0, "no": 0}

    def vote(self, choice: str):
        if choice in self.votes:
            self.votes[choice] += 1

    def result(self):
        return "approved" if self.votes["yes"] > self.votes["no"] else "rejected"


class AI_Governance:
    def __init__(self):
        self.proposals = []

    def submit(self, title, description, proposer):
        p = Proposal(title, description, proposer)
        self.proposals.append(p)
        return p

    def list_proposals(self):
        return [p.title for p in self.proposals]
