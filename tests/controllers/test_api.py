import json


def test_booksinfo(test_client):
    res = test_client.get('/api/booksinfo',headers={'rows': '4'})
    assert res.status_code == 200
    assert type(res.json['books']) == list
    assert res.json['books'][0]['id']==7
    assert 'message' not in res.json
# def test_booksinfo_empty_rows(test_client):
    res1 = test_client.get('/api/booksinfo',headers={'rows': ''})
    assert res1.status_code == 200
    assert type(res1.json['books']) == list
    assert res1.json['books'][0]['id']==7
    assert 'message' not in res1.json
def test_booksinfoe_fail(test_client):
    fail_res = test_client.get('/api/booksinfo',headers={'rows': 'a'})
    assert fail_res.status_code == 500
    assert fail_res.json['message']=='please pass only numbers or empty string'
    assert fail_res.json['success']==False
# def test_booksinfo_keyerror(test_client):
    empty_res = test_client.get('/api/booksinfo',headers={})
    assert empty_res.status_code == 500
    assert empty_res.json['message']=='please pass no of rows through headers'
    assert empty_res.json['success']==False
    
    
    # assert expected == json.loads(res.get_data(as_text=True))
def test_valid_signin(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/signin' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/api/signin',
                                json={"username":'book_management@admin.com', "password":'Welcome@123'}
                                )
    assert response.status_code == 200
    assert 'Successfully logged in as book_management@admin.com' in response.json['message']
    assert 'Book Management' in response.json['data']
    assert 'Login' not in response.json['data']
    

def test_invalid_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/siginin' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/api/signin',
                                json={'username':'book_management@admin.com', 'password':'Welco@123'})
   
    assert response.status_code == 500
    assert 'Invalid password' in response.json['message']
    response = test_client.post('/api/signin',
                                json={'username':'book_managemen@admin.com', 'password':'Welco@123'})
    assert 'Invalid username' in response.json['message']

