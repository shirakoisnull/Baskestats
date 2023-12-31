<!-- TeamUpdate.svelte -->
<script>
  import { navigate } from 'svelte-routing';
  import { onMount } from 'svelte';

  let player = {
    teamId: -1,
    name: '',
    age: '',
    height: 0,
    weight: 0,
    pointsScored: 0,
  };

  onMount(() => {
    // Get the team data passed through the route
    const { player: routePlayer} = history.state;

    // If routeTeam exists (coming from TeamManagement), update the team data
    if (routePlayer) {
      player = { ...routePlayer};
    }
  });

  function handleSubmit() {
    // Logic for handling form submission (to be implemented)
    console.log('Updated Player Details:', player);
    // You can add logic to save or send updated data here

    // For demonstration purposes, navigate back to TeamManagement
    navigate('/player');
  }

  function handleCancel() {
    // Redirect back to TeamManagement page on cancel
    navigate('/players');
  }
</script>

<style>
  /* Style for vertical alignment and centering */
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 65vh;
    gap: 12px; /* Adjust vertical gap between form elements */
  }

  label {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 300px; /* Adjust maximum width of form elements */
  }

  input,
  button {
    padding: 8px;
    margin-top: 6px;
    font-size: 1em;
    width: calc(
      100% - 16px
    ); /* Match the width of input/button to label width */
    /* Subtracting 16px (padding) from the width to account for padding */
  }

  button {
    margin-top: 5px; /* Adjust top margin of the buttons */
  }
</style>

<h1>Update Player</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Player Name:
    <input type="text" bind:value={player.name} />
  </label>
  <label>
    Player Age:
    <input type="number" bind:value={player.age} />
  </label>
  <label>
    Player Height:
    <input type="number" bind:value={player.height} />
  </label>
  <label>
    Player Weight:
    <input type="number" bind:value={player.weight} />
  </label>
  <label>
    Points Scored:
    <input type="number" bind:value={player.pointsScored} />
  </label>
  <button type="submit">Update</button>
  <button type="button" on:click={handleCancel}>Cancel</button>
</form>