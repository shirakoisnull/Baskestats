<!-- ConfirmationModal.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  
  export let teamName = '';
  const dispatch = createEventDispatcher();
  function confirmAction(action) {
    dispatch('confirm', action);
  }
</script>
<style>
  /* Style your modal here */
  /* Example styles; modify as needed */
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(19, 19, 19, 0.901);
    padding: 20px;
    border: 1px solid #ff3e00aa;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
    z-index: 1000;
  }
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
  }
</style>
<div class="modal-overlay" on:click={() => confirmAction(false)}></div>
<div class="modal">
  <p>Are you sure you want to delete {teamName}?</p>
  <button class="delete-button" on:click={() => confirmAction(true)}>Yes</button>
  <button on:click={() => confirmAction(false)}>No</button>
</div>