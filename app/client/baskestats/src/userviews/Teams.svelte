<script>
  import { fetchTeams, viewTeam } from "../api.js";
  import { onMount } from "svelte";

  let teams = [];
  let searchQuery = '';

  onMount(async () => {teams = await fetchTeams();});

  async function handleView(tId){
    let selTeam = await viewTeam();
  }

  $: visibleTeams = searchQuery ?
    teams.filter(team => {
      return (
        team[1].toLowerCase().includes(searchQuery.toLowerCase())
        // Replace 'team.name' with the property you want to filter/search by
      );
    }) : teams;
</script>

<input type="text" bind:value={searchQuery} placeholder="Search teams..." />
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>City</th>
      <th>Wins</th>
      <th>Losses</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each visibleTeams as team}
      <tr>
        <td>{team[1]}</td>
        <td>{team[2]}</td>
        <td>{team[3]}</td>
        <td>{team[4]}</td>
        <td>
            <button on:click={() => handleView(team[0])}>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>