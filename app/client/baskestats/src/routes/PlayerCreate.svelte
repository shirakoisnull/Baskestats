<script>
  import { navigate } from "svelte-routing";
  
  let player = {
    pId: '',
    tId: '',
    pName: '',
    pAge: '',
    pHeight: '',
    pWeight: '',
    pScore: ''
  };

  async function handleSubmit() {
 try {
      const response = await fetch('http://127.0.0.1:5002/players', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          pName: player.pName,
          pAge: player.pAge,
          pHeight: player.pHeight,
          pWeight: player.pWeight,
          pPoints: player.pScore,
          teamId: player.tId
        })
      });

      if (response.ok) {
        console.log('Player created successfully!');
        // Perform any necessary actions upon successful creation
      } else {
        console.error('Failed to create player:', response.statusText);
      }
    } catch (error) {
      console.error('Error creating player:', error);
    }
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
    <input type="text" bind:value={player.pName} />
  </label>
  <label>
    Age:
    <input type="number" min="0" bind:value={player.pAge} />
  </label>
  <label>
    Height:
    <input type="number" min="0" bind:value={player.pHeight} />
  </label>
  <label>
    Weight:
    <input type="number" min="0" bind:value={player.pWeight} />
  </label>
  <label>
    Points Scored:
    <input type="number" min="0" bind:value={player.pScore} />
  </label>
  <label>
    Team ID (optional):
    <input type="number" min="0" bind:value={player.tId} />
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
    height: 75vh;
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
    text-align: center;
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
