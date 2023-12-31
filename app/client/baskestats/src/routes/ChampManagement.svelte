<script>
 // import ConfirmationModal from "../ConfirmationModal.svelte";
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  // TODO: add player to team association logic
//   let showModal = false;
//   let selectedPlayer = null;
  // Assuming teamsData contains your team entries, fetched from somewhere
  let champData= [
    {
        cid: 1,
        year: 2011,
    },
    {
        cid: 2,
        year: 2001,
    },
    // Add more entries as needed
  ];
  // Initialize teams as an empty array
  let championships = [];

  // Fetch teams data from the backend
  async function fetchChampionships() {
    try {
      const response = await fetch("http://127.0.0.1:5002/players"); // Replace with your API endpoint
      if (response.ok) {
        const playerData = await response.json();

        // Assuming the structure is [[team_id, team_name, team_city, team_wins, team_losses], ...]
        championships = champData.map((champ) => ({
          cid: champ[0],
          year: champ[1],
        }));

        // teams array assumed to be an array of objects with specific properties for each team
      } else {
        console.error("Failed to fetch players:", response.status);
        // Handle error
      }
    } catch (error) {
      console.error("Error fetching players:", error);
      // Handle error
    }
  }

  // Fetch player data on component mount
  onMount(fetchChampionships);

  function handleClick(event) {
    navigate("/newchamp");
  }

  function deleteChamp(champ) {
    const confirmation = window.confirm(`Are you sure you want to delete championship #${champ.cid}?`);
    if (confirmation) {
      champData = champData.filter(c => c.cid !== champ.cid);
    }
  }
  // CURSED STUFF
  // function deleteTeam(player) {
  //   selectedPlayer = player;
  //   showModal = true;
  // }

  // function handleConfirmDelete(confirm) {
  //   if (confirm) {
  //     // Implement deletion logic
  //     playerData = playerData.filter(player => player.id !== selectedPlayer.id);
  //     // After deletion or on cancel, hide the modal
  //     showModal = false;
  //   } else {
  //     // On cancel, hide the modal
  //     showModal = false;
  //   }
  // }
  function handleUpdate(champ) {
    navigate(`/editchamp`, { state: { champ } });
  }
</script>

<!-- CURSED -->
<!-- {#if showModal}
  <ConfirmationModal
    displayName={selectedPlayer.name}
    on:confirm={handleConfirmDelete}
  />
{/if} -->

<h1>Championship Management</h1>

<div>
  <button on:click={handleClick}>Create New Championship</button>
</div>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Year</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each champData as champ}
      <tr>
        <td>{champ.cid}</td>
        <td>{champ.year}</td>
        <td>
          <button on:click={() => handleUpdate(champ)}>Update</button>
          <button class="delete-button" on:click={() => deleteChamp(champ)}>Delete</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<button class="back-button" on:click={() => navigate("/secretary")}>Go Back</button>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin: auto; /* Center the table horizontally */
  }

  th,
  td {
    padding: 10px;
    border: 1px solid #ccc;
    text-align: left;
  }

  th {
    /* background-color: #f2f2f2; */
    font-weight: bold;
  }

  tr:hover {
    background-color: #e9e9e921;
  }

  /* Style for update and delete buttons */
  button {
    padding: 6px 10px;
    margin: 2px;
    cursor: pointer;
    color: white;
    /* border: none; */
    border-radius: 4px;
  }

   /* Style the back button */
   .back-button {
    position: absolute;
    top: 20px;
    left: 20px;
    padding: 10px;
    background-color: #ff4000;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

</style>
