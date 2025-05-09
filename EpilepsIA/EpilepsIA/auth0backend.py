import requests 
from social_core.backends.oauth import BaseOAuth2 

class Auth0(BaseOAuth2): 
    """Auth0 OAuth authentication backend""" 
    name = 'auth0' 
    SCOPE_SEPARATOR = ' ' 
    ACCESS_TOKEN_METHOD = 'POST' 
    EXTRA_DATA = [ ('picture', 'picture') ] 
    
    def authorization_url(self): 
        """Return the authorization endpoint.""" 
        return "https://" + self.setting('DOMAIN') + "/authorize" 
    
    def access_token_url(self): 
        """Return the token endpoint.""" 
        return "https://" + self.setting('DOMAIN') + "/oauth/token" 
    
    def get_user_id(self, details, response): 
        """Return current user id.""" 
        return details['user_id'] 
    
    def get_user_details(self, response): 
        url = 'https://' + self.setting('DOMAIN') + '/userinfo' 
        headers = {'authorization': 'Bearer ' + response['access_token']} 
        resp = requests.get(url, headers=headers) 
        userinfo = resp.json() 
        
        return {'username': userinfo['nickname'], 'first_name': userinfo['name'], 'picture': userinfo['picture'], 'user_id': userinfo['sub']}
    
    # Esta función está POR FUERA de la clase Auth0. Es una función independiente.

    def getRole(request):

        user = request.user 
        auth0user = user.social_auth.filter(provider="auth0")[0]
        accessToken = auth0user.extra_data['access_token'] 
        url = "https://dev-qox2s5e2aky6aehb.us.auth0.com.auth0.com/userinfo" 
        headers = {'authorization': 'Bearer ' + accessToken}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()
        role = userinfo['dev-qox2s5e2aky6aehb.us.auth0.com/role']

        return (role)