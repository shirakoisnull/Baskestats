<script>
  import { navigate } from "svelte-routing";
  import { onMount } from "svelte";
  import { fetchTeams } from '../api.js'; 
  
  let player = {
    pid: 0,
    tid: '',
    name: '',
    age: 0,
    height: 0,
    weight: 0,
    pointsScored: 0,
  };

  let teams = [];

  onMount(() => {
    
    // Get the player data passed through the route
    const { player: routePlayers } = history.state;

    if (routePlayers) {
      player = { ...routePlayers };
    }
  });

 onMount(async () => {
    teams = await fetchTeams();
  });

  async function handleSubmit() {
    // Logic for handling form submission (to be implemented)
    try {
      console.log("Sending Player Data:", player); // Log the player object before sending the request

      const response = await fetch(
        `http://127.0.0.1:5002/players/${player.pid}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            pName: player.name,
            pAge: player.age,
            pHeight: player.height,
            pWeight: player.weight,
            pPoints: player.pointsScored,
            teamId: player.tid
          }),
        }
      );

      if (response.ok) {
        // Perform any necessary actions upon successful creation
        console.log("Updated Player Details:", player);
        navigate("/players");
      } else {
        console.error("Failed to update player:", response.statusText);
      }
    } catch (error) {
      console.error("Error updating player:", error);
    }
  }

  function handleCancel() {
    // Redirect back to TeamManagement page on cancel
    navigate("/players");
  }
</script>

<h1>Update Player</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Player Name:
    <input type="text" bind:value={player.name} />
  </label>
  <label>
    Player Age:
    <input type="number" min="0" bind:value={player.age} />
  </label>
  <label>
    Player Height:
    <input type="number" min="0" bind:value={player.height} />
  </label>
  <label>
    Player Weight:
    <input type="number" min="0" bind:value={player.weight} />
  </label>
  <label>
    Points Scored:
    <input type="number" min="0" bind:value={player.pointsScored} />
  </label>
  <!-- <label>
    Plays On (Team ID):
    <input type="number" min="0" bind:value={player.tid} />
  </label> -->
 <label>
    Team (optional):
    <select bind:value={player.tid}>
      {#each teams as team, index}
        <option value={team[0]}>{team[0]} - {team[1]}</option>
      {/each}
    </select>
  </label>
  <button class="submit-button" type="submit">Update</button>
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
