import Ember from 'ember';

export default Ember.Route.extend({
  beforeModel: function(transition) {
    if (!this.controllerFor('auth').get('hasValidToken')) {
      this.transitionTo('auth');
    }
  }
});
