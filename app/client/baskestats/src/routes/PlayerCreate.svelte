<!-- TeamCreate.svelte -->
<script>
  import { navigate } from "svelte-routing";
  
  let playerName = "";
  let playerAge = '';
  let playerHeight = '';
  let playerWeight = '';
  let playerPoints = ''; 

  function handleSubmit() {
    // Logic for handling form submission (to be implemented)
    // Example: Send data to API, perform validation, etc.
    console.log("Submitted!", { playerName, playerAge, playerHeight, playerWeight, playerPoints });
    // You can add logic to save or send data here

    // For demonstration purposes, navigate back to TeamManagement
    navigate("/players");
  }

  function handleCancel() {
    // Redirect back to TeamManagement page on cancel
    navigate("/players");
  }
</script>

<h1>New Player</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Name:
    <input type="text" bind:value={playerName} />
  </label>
  <label>
    Age:
    <input type="number" bind:value={playerAge} />
  </label>
  <label>
    Height:
    <input type="number" bind:value={playerHeight} />
  </label>
  <label>
    Weight:
    <input type="number" bind:value={playerWeight} />
  </label>
  <label>
    Points Scored:
    <input type="number" bind:value={playerPoints} />
  </label>
  <button class="submit-button" type="submit">Submit</button>
  <button type="button" on:click={handleCancel}>Cancel</button>
</form>

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
