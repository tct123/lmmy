from pythorhead import Lemmy

with open(file="password.txt",mode="rb") as f:
    pw = f.read()
with open(file="usernameoremail.txt",mode="rb") as f:
    ue = f.read()
with open(file="url.txt",mode="rb") as f:
    url = f.read()

lemmy = Lemmy(api_base_url=url)
lemmy.log_in(username_or_email=ue,password=pw)
community_id = lemmy.discover_community("tcdiy")
lemmy.post.create(community_id=community_id,name="Hallo Welt")