from src.governance.aviatorx import AI_Governance

def test_submit_proposal():
    gov = AI_Governance()
    p = gov.submit("Test", "This is a test", "0xABC")
    assert p.title == "Test"
    assert p.result() == "rejected"  # No votes yet

def test_voting():
    gov = AI_Governance()
    p = gov.submit("Upgrade", "Add new flight lanes", "0xABC")
    p.vote("yes")
    assert p.result() == "approved"
