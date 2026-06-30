const Card_container = document.getElementById("Card_container");

// fetch data =============================================================
async function fetchData() {
  try {
    const response = await fetch(
      "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a",
    );
    const data = await response.json();
    showData(data.drinks);
  } catch (error) {
    console.error("Error", error);
  }
}

// fetch data by search =========================================================

const searchBtn = document.getElementById("Search");

searchBtn.addEventListener("click", (event) => {
  event.preventDefault();
  const search_input = document.getElementById("Search_input").value;
  Card_container.innerHTML = "";
  if (search_input == "") {
    fetchData();
  } else {
    async function SearchFetchData() {
      try {
        const response = await fetch(
          `https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${search_input}`,
        );
        const data = await response.json();
        console.log(data);
        if(data.drinks == null){
          const div = document.createElement("div");

div.className = "d-flex justify-content-center w-100";

div.innerHTML = `
    <p class="fs-4 text-danger">
        Not found in any search result.
    </p>
`;

Card_container.appendChild(div);
          return;
        }
        showData(data.drinks);
      } catch (error) {
        console.error("Error", error);
      }
    }

    SearchFetchData();
  }
});

// show data in card =======================================================

function showData(products) {
  Card_container.innerHTML = "";

  products.forEach((product) => {
    const div = document.createElement("div");
    div.innerHTML = `
        <div class="card" style="width: 18rem;">
  <img src=${product.strDrinkThumb} class="card-img-top " alt="..." style="height: 200px;">
  <div class="card-body">
    <h5 class="card-title">Name : ${product.strDrink} </h5>
    <p class="card-text">Category : ${product.strCategory} </p>
    <p class="card-text text-truncate"> ${product.strInstructions}</p>
    <div class="d-flex justify-content-between">
      <button onclick="addToCart({
    strDrink: '${product.strDrink}',
    strDrinkThumb: '${product.strDrinkThumb}'
})"  class="btn btn-primary"> Add to group</button>
      <button
onclick="handleDetails(
'${product.strDrink}',
'${product.strCategory}',
'${product.strAlcoholic}',
'${product.strInstructionsES}',
'${product.strDrinkThumb}'
)"
data-bs-toggle="modal"
data-bs-target="#detailsModal"
class="btn btn-primary">
Details
</button>
    </div>
  </div>
</div>
        `;
    Card_container.appendChild(div);
  });
}

fetchData();

// Details ===================================================================

function handleDetails(name, category, alcohol, instruction, img) {
  document.getElementById("modalTitle").innerText = name;

  document.getElementById("modalCategory").innerText = category;

  document.getElementById("modalAlcohol").innerText = alcohol;

  document.getElementById("modalInstruction").innerText = instruction;

  document.getElementById("modalImg").src = img;
}

// add to cart ========================================================
let cartCount = 0;
function addToCart(product) {
   if (cartCount >= 7) {
        alert("You can only add 7 items to the cart.");
        return;
    }
    cartCount++;

        document.getElementById("count-cart").innerText = cartCount;

    const cartBody = document.getElementById("cart-body");

    const tr = document.createElement("tr");

     tr.innerHTML = `
        <th scope="row">${cartCount}</th>
        <td>
            <img src="${product.strDrinkThumb}"
                 width="50"
                 height="50"
                 style="object-fit:cover;">
        </td>
        <td>${product.strDrink}</td>
    `;
    cartBody.appendChild(tr);
}
