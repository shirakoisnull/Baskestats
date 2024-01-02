<script>
  import { navigate } from "svelte-routing";

 let team = {
    tName: '',
    tCity: '',
    tWins: 0,
    tLosses: 0
  };

 async function handleSubmit() {
    // Logic for handling form submission (to be implemented)
    // Example: Send data to API, perform validation, etc.
 try {
      const response = await fetch('http://127.0.0.1:5003/teams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tName: team.tName,
          tCity: team.tCity,
          tWins: team.tWins,
          tLosses: team.tLosses
        })
      });

      if (response.ok) {
        console.log('Team created successfully!');
        // Perform any necessary actions upon successful creation
      } else {
        console.error('Failed to create team:', response.statusText);
      }
    } catch (error) {
      console.error('Error creating team:', error);
    }
    navigate("/teams");
  }
    // console.log("Submitted!", { teamName, teamCity, teamWins });
    // You can add logic to save or send data here

    // For demonstration purposes, navigate back to TeamManagement
  

  function handleCancel() {
    // Redirect back to TeamManagement page on cancel
    navigate("/teams");
  }
</script>

<h1>New Team</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Team Name:
    <input type="text" bind:value={team.tName} />
  </label>
  <label>
    Team City:
    <input type="text" bind:value={team.tCity} />
  </label>
  <label>
    Team Wins:
    <input type="number" bind:value={team.tWins} />
  </label>
  <label>
    Team Losses:
    <input type="number" bind:value={team.tLosses} />
  </label>
  <button type="submit" class="submit-button">Submit</button>
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
