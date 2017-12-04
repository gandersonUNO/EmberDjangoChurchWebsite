import Controller from '@ember/controller';

export default Controller.extend({
  actions: {

    /* Dialog */
    openDialog(item, event) {
      this.set('selectedEvent', item);
      this.set('showDialog', true);
    },

    closeDialog(result) {
      location.reload();
    },


  }
});
