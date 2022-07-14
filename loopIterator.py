"""
for (int ci = 0; ci < clubs.size(); ci++)
    for (int mi = 0; mi < clubs[ci].members.size(); mi++)
        for (int ui = 0; ui < users.size(); ui++)

            if (clubs[ci].members[mi] == users[ui])
            cout << "user[" << j<< "] is in club[" << i<< "]" << endl;
"""


club={1:['kadowaki','isida','okabe'],2:['yamanaka','hayakawa'],3:['tatibana','kimura']}
user= ['yamanaka','kimura','hayakawa','isida','tatibana','kadowaki','okabe']

for ui in user:
    for ci,cv in club.items():
        for mi in cv:
            if ui == mi:
                print(ui + 'はクラブ' + str(ci))