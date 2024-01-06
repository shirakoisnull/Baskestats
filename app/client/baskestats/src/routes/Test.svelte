<script>
  import Modal from "../MatchModal.svelte";
  import { fetchMatches } from "../api.js";
  import { onMount } from "svelte";

  let showModal = false;
  let fetchedResults = []; // Results fetched from backend
    let cId = -1;

  onMount(async () => {
    fetchedResults = await fetchMatches(cId);
  });

  function displayModal() {
    showModal = true;
  }
</script>

<button on:click={displayModal}>View</button>

{#if showModal}
  <Modal
    {showModal}
    results={fetchedResults}
    closeModal={() => (showModal = false)}
  />
{/if}

<style>
  button {
    padding: 6px 10px;
    margin: 2px;
    cursor: pointer;
    color: white;
    /* border: none; */
    border-radius: 4px;
  }
</style>
