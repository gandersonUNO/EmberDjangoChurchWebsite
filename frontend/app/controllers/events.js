import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    clicked(event){
      alert(event);
    }
  }
});
