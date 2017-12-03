import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.bURL
});

Router.map(function() {
  this.route('login');
  this.route('about');
  this.route('church');
  this.route('believe');
  this.route('childrens');
  this.route('youth');
  this.route('events');
});

export default Router;
