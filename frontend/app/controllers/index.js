import Ember from 'ember';

export default Ember.Controller.extend({
  toggleAlert: function(alert) {
    if (alert.get('length') > 0) {
      return true;
    }
    else {
      return false;
    }
  }
});
