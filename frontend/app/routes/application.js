import Ember from 'ember';

export default Ember.Route.extend({
  getSermons(){
    var items = Ember.A([]);
    return Ember.$.get('/api/sermons').then(function(sermons){
      sermons.forEach(function(sermon){
        // console.log(event);
        items.addObject({
          id: sermon.pk,
          description: sermon.fields.description,
          document: sermon.fields.document,
        });
      });
      return items.reverse()
    }, function(msg){//error
      console.log('Error loading alerts:');
      console.log(msg.statusText);
    });
  },
  model() {
    return this.getSermons();
  },
  setupController(controller, model){
    this._super(controller, model);
    var route = this;
    setInterval(Ember.run.later(route, function() {
      // code here will execute within a RunLoop about every minute
      if(controller.get('auth.isLoggedIn')){
        route.getData().then(function(data){
          if(data[0].id!=controller.get('content')[0].id){
            controller.get('content').insertAt(0, data[0]);
          }
        });
      }
    }, 5), 3000);
  }
});
