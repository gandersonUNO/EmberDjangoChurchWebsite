import Route from '@ember/routing/route';
import Ember from 'ember';

export default Route.extend({
  model: function() {
    return {
      events: Ember.A([{
        title: 'Evening Service',
        start: '2017-11-04T17:30:00',
        end: '2017-11-04T18:30:00'
      }, {
        title: 'Morning Service',
        start: '2017-11-05T10:30:00',
        end: '2017-11-05T11:30:00'
      }, {
        title: 'Morning Service',
        start: '2017-11-05T08:00:00',
        end: '2017-11-05T09:0:00'
      }])
    };
  }
});
