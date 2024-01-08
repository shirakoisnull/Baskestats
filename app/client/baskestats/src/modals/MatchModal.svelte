<script>
  export let showModal = false;
  export let results = [];
  export let curChamp;
  export let closeModal = () => {};
  import { fetchMatches, setScore } from "../api";
  // import { onMount, onDestroy } from 'svelte';

  let modifiedScores = [];

  $: modifiedScores = results.map((result) => {
    if (result[5]) {
      return result[5].split(",").map(() => "");
    }
    return [];
  });

  function handleInput(event, rowIndex, scoreIndex) {
    // modifiedScores[rowIndex][scoreIndex] = event.target.value;
    const inputValue = event.target.value;
    // Ensure the input value is not undefined or null
    const validValue = inputValue ? parseInt(inputValue) : 0;
    // Ensure the value is not negative
    modifiedScores[rowIndex][scoreIndex] = validValue >= 0 ? validValue : 0;
  }

  async function handleUpdate(match_id, matchresult_ids, rowIndex) {
    const separateIds = matchresult_ids.split(",");

    for (const [i, matchresult_id] of separateIds.entries()) {
      let score = modifiedScores[rowIndex][i];
      // Ensure blank inputs are treated as 0
      score = score === "" ? 0 : score;
      // const score = modifiedScores[rowIndex][i];
      // Call your API function to update score for the current matchresult_id
      // NA SAI KALA RE GPT
      await setScore(matchresult_id, match_id, parseInt(score));
      results = await fetchMatches(curChamp);
      // Handle API response or error here
    }
  }
</script>

{#if showModal}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="modal-overlay" on:click={closeModal}></div>

  <div class="modal">
    <!-- svelte-ignore a11y-no-static-element-interactions -->

    <div class="modal-content">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <button class="logout-button" on:click={closeModal}>X</button>
      <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Location</th>
            <th>Date</th>
            <th>Time</th>
            <th>Team 1</th>
            <th>Team 2</th>
            <th> Score </th>
          </tr>
        </thead>
        <tbody>
          {#each results as result, rowIndex}
            <tr>
              <td>{result[1]}</td>
              <td>{result[2]}</td>
              <td>{result[3]}</td>
              {#if result[4]}
                {#each result[4].split(",") as value}
                  <td>{value}</td>
                {/each}
              {/if}
              {#if result[5]}
                <td>{result[5].replace(/,/g, "-")}</td>
              {/if}
              <td>
                {#if result[5]}
                  {#each result[5].split(",") as score, scoreIndex}
                    <input
                      class="score-input"
                      type="number"
                      placeholder="Team {scoreIndex + 1}"
                      value={modifiedScores[rowIndex][scoreIndex]}
                      on:input={(event) =>
                        handleInput(event, rowIndex, scoreIndex)}
                    />
                  {/each}
                {/if}
              </td>

              <td>
                <button
                  on:click={() => handleUpdate(result[0], result[6], rowIndex)}
                >
                  Update
                </button>
              </td>
            </tr>{/each}
        </tbody>
      </table>
    </div>
  </div>
  </div>
{/if}

<style>
  .score-input {
    display: flex;
    background-color: #2424242e;
    height: 1.7em;
    margin: auto;
    border-radius: 4px;
    border: 1px solid #ff4000;
    padding: 0 0.5em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    /* background-color: ; */
    cursor: pointer;
    transition: border-color 0.25s;
    width: 100;
  }
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(19, 19, 19, 0.901);
    padding: 20px;
    border: 1px solid #ff3e00;
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
