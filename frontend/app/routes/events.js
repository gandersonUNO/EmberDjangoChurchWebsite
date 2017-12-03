import Ember from 'ember';

export default Ember.Route.extend({
  getData(){
    var items = Ember.A([]);
    return Ember.$.get('/api/churchevents').then(function(events){
      events.forEach(function(event){
        // console.log(event);
        items.addObject({
          id: event.pk,
          title: event.fields.title,
          start: event.fields.starttime,
          end: event.fields.endtime,
          description: event.fields.description,
          address: event.fields.address
        });
      });
      return items.reverse()
    }, function(msg){//error
      console.log('Error loading events:');
      console.log(msg.statusText);
    });
  },
  model() {
    return this.getData();
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
