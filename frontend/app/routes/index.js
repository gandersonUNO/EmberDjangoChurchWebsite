import Ember from 'ember';


export default Ember.Route.extend({
  getData(){
    var items = Ember.A([]);
    return Ember.$.get('/api/alerts').then(function(alerts){
      alerts.forEach(function(alert){
        // console.log(event);
        items.addObject({
          id: alert.pk,
          text: alert.fields.text,
          start: alert.fields.startdate,
          end: alert.fields.enddate
        });
      });
      return items.reverse()
    }, function(msg){//error
      console.log('Error loading alerts:');
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
