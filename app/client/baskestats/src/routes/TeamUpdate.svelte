<!-- TeamUpdate.svelte -->
<script>
  import { navigate } from 'svelte-routing';
  import { onMount } from 'svelte';

  let team = {
    id: null,
    name: '',
    city: '',
    wins: 0,
    losses: 0
  };

  onMount(() => {
    // Get the team data passed through the route
    const { team: routeTeam } = history.state;

    // If routeTeam exists (coming from TeamManagement), update the team data
    if (routeTeam) {
      team = { ...routeTeam };
    }
  });

  function handleSubmit() {
    // Logic for handling form submission (to be implemented)
    console.log('Updated Team Details:', team);
    // You can add logic to save or send updated data here

    // For demonstration purposes, navigate back to TeamManagement
    navigate('/teams');
  }

  function handleCancel() {
    // Redirect back to TeamManagement page on cancel
    navigate('/teams');
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

<h1>Update Team</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Team Name:
    <input type="text" bind:value={team.name} />
  </label>
  <label>
    Team City:
    <input type="text" bind:value={team.city} />
  </label>
  <label>
    Team Wins:
    <input type="number" bind:value={team.wins} />
  </label>
  <label>
    Team Losses:
    <input type="number" bind:value={team.losses} />
  </label>
  <button type="submit">Update</button>
  <button type="button" on:click={handleCancel}>Cancel</button>
</form>