from .server import Server, server_list


def test_checkTop100():
    for server in server_list:

        # Read the top 100 info
        top100 = server.getTop100()
        print(server.region.name, server.server_id)

        # Quick check to ensure user data is being sent
        assert top100[0].get("nickname", None) != None

