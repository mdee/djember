import Ember from 'ember';

export default Ember.Component.extend({
  name: null,
  path: null,
  tagName: 'li',
  classNameBindings: ['isActive:active'],
  isActive: function(){
    return this.get('name') === this.get('path');
  }.property('path')
});
