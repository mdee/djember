import Ember from 'ember';
import ENV from '../config/environment';

export default Ember.ObjectController.extend({
  email: null,
  password: null,
  token: null,
  errors: null,
  reset: function() {
    this.setProperties({
      email: null,
      password: null,
      errors: null,
      model: null
    });
  },
  hasValidToken: function() {
    var token = this.get('token');
    return (!Ember.isEmpty(token) && token != 'null' && token !== 'undefined');
  }.property('token'),
  setupAjax: function() {
    var self = this, token = this.get('token');
    console.log('hi', token);
    Ember.$(document).ajaxSend(function(event, xhr, settings) {
      if (self.get('hasValidToken')) {
        xhr.setRequestHeader('Authorization', 'Token ' + token);
      }
    });
  },
  setCurrentUser: function() {
    if (this.get('hasValidToken')) {
      var currentUser = this.store.find('user', 'me');
      this.set('model', currentUser);
    } else {
      this.reset();
    }
  },
  tokenChanged: function() {
    localStorage.APP_auth_token = this.get('token');
    this.setupAjax();
    this.setCurrentUser();
  }.observes('token'),
  actions: {
    login: function() {
      var self = this;
      var data = this.getProperties('email', 'password');
      Ember.$.post(ENV.APP.API_HOST + '/api-token-auth/', data, null, 'json').then(
          function(response) {
            self.reset();
            self.set('token', response.token);
            self.transitionToRoute('index');
          },
          function(jqXHR, status, error) {
            self.set('errors', Ember.$.parseJSON(jqXHR.responseText));
          }
      );
    }
  }
});
