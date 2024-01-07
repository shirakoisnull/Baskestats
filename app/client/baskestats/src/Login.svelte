<script>
  import { navigate } from "svelte-routing";
  import { onMount } from "svelte";
  export let showLogin= false;
  export let closeModal = () => {};


  let username = "";
  let password = "";
  let isAuthenticated = false; // Track user authentication status
  let storedUsername = "";
  let wrongCredentials = false;
  

  async function handleSubmit() {
    try {
      const response = await fetch("http://127.0.0.1:5001/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });
console.log(response);
      if (response.ok) {
        const contentType = response.headers.get("content-type");
        console.log(contentType);
        if (contentType && contentType.includes("application/json")) {
          
          const responseData = await response.json();
          console.log(responseData);
          if (responseData.access_token && responseData.username) {
            const { access_token, username } = responseData;
            localStorage.setItem("jwtToken", access_token);
            localStorage.setItem("username", username);
            isAuthenticated = true;
            
            storedUsername = username;

            // If login is successful, navigate to SecretaryPanel
            
            navigate("/secretary");
            closeModal();
          } else {
            console.log(responseData);
            alert("Unexpected response format");
          }
        } else {
          const errorMessage = await response.text();
          if (errorMessage === "Error") {
            wrongCredentials = true;
          } else {
            alert("Unexpected error");
          }
        }
      } else {
        console.error("Error:", response.status);
        alert("Failed to log in");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while logging in");
    }
  }

  onMount(() => {
    const token = localStorage.getItem("jwtToken");
    if (token) {
      isAuthenticated = true;
    }
  });

</script>
{#if showLogin}
  <!-- <button on:click={() => closeTest()}>CLICK</button> -->
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="modal-overlay" on:click={closeModal}></div>
  <div class="modal">
    <!-- svelte-ignore a11y-no-static-element-interactions -->

  <!-- <button on:click={() => closeTest()}>CLICK</button> -->
    <div class="modal-content">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- <span class="close" on:click={closeModal}>&times;</span> -->

{#if wrongCredentials}
  <h2 style="color: crimson;">Wrong credentials</h2>
{/if}

<form on:submit|preventDefault={handleSubmit} class="login">
  <label>
    <p>Username</p>
    <input type="text" placeholder="Enter your username" bind:value={username} />
  </label>
  <label>
    <p>Password</p>
    <input type="password" placeholder="Enter your password" bind:value={password} />
  </label>
  <button class="submit-button"type="submit">Login</button>
</form>
    </div>
    </div>
{/if}

<style>
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(19, 19, 19, 0.901);
    padding: 20px;
    border: 1px solid #ff3e00;
    border-radius: 50%;
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
