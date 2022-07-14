"""
for (int ci = 0; ci < clubs.size(); ci++)
    for (int mi = 0; mi < clubs[ci].members.size(); mi++)
        for (int ui = 0; ui < users.size(); ui++)

            if (clubs[ci].members[mi] == users[ui])
            cout << "user[" << j<< "] is in club[" << i<< "]" << endl;
"""


club={1:['kadowaki','isida','okabe'],2:['yamanaka','hayakawa'],3:['tatibana','kimura']}
user= ['yamanaka','kimura','hayakawa','isida','tatibana','kadowaki','okabe']

for user_name in user:
    for cn,cm in club.items():
        for member_name in cm:
            if user_name == member_name:
                print(user_name + 'はクラブ' + str(cn))