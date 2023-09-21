import puppeteer from "puppeteer";
import fs from "fs";

(async () => {
  const jsonData = "./pt-br/top.json";
  const jsonData_new = "top-en.json";

  const data_infor = "./top-en.json";
  const data_infor_new = "./top-new.json";

  // const teste = "./teste.json";
  // const teste_2 = "./teste_2.json";

  let result = [];

  await fs.readFile(data_infor, "utf8", async (error, data) => {
    if (error) {
      // console.error('Erro ao ler o arquivo JSON:', error);
      return;
    }

    // Agora você pode usar os dados do arquivo JSON, que estão em 'data'
    const jsonData = JSON.parse(data);
    // Launch the browser and open a new blank page
    const sleep = (ms) => {
      return new Promise((resolve) => setTimeout(resolve, ms));
    };

    const divinepride = async (object) => {
      console.log("====================================");
      console.log("divinepride: ", object);
      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      const url = `https://www.divine-pride.net/database/item/${object.id}`;
      console.log("====================================");
      console.log("divinepride - url: ", url);
      await page.goto(url);

      const elements = await page.evaluate(() => {
        return {
          TypeItem: document
            .getElementsByClassName(
              "table table-bordered table-striped table-condensed table-full table-small-text"
            )[0]
            .getElementsByTagName("tr")[4]
            .getElementsByTagName("td")[0].innerText,
        };
      });

      let textoTypo = elements.TypeItem;
      // Substituir a palavra "específica" por "novaPalavra"
      let novoTextoTOPO = textoTypo.replace("Upper", "TOPO");
      let novoTextoTOPOeMEIO = novoTextoTOPO.replace("Middle", "MEIO");
      elements.TypeItem = novoTextoTOPOeMEIO.split(`/`);

      await browser.close();
      const returnedTarget = Object.assign(object, elements);
      return returnedTarget;
    };

    const playragnarokonlinebr = async (object) => {
      try {
        console.log("====================================");
        console.log("playragnarokonlinebr: ", object);
        console.log("====================================");
  
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.goto(object.link);
  
        const elements = await page.evaluate(() => {
          return {
            TypeItem: document
              .getElementsByClassName("items-emphasis")[0]
              .innerText.split("Equipa em")[1]
              .split("\nPeso")[0],
            TypeItemNew: [],
          };
        });
  
        let novoTextoTOPO = "Topo";
        let novoTextoMEIO = "Meio";
  
        let textoTypo = elements.TypeItem;
  
        if (textoTypo.toLowerCase().includes(novoTextoTOPO.toLowerCase())) {
          elements.TypeItemNew.push("TOPO");
        }
  
        if (textoTypo.toLowerCase().includes(novoTextoMEIO.toLowerCase())) {
          elements.TypeItemNew.push("MEIO");
        }
  
        await browser.close();
        const returnedTarget = Object.assign(object, elements);
        return returnedTarget;
      } catch (error) {
        return "";
      }
     
    };

    for (let index = 0; index < jsonData.length; index++) {
      const dataItem = jsonData[index];

      if (dataItem.id === 0) {
        continue;
      }

      if (typeof dataItem.link === "undefined") {
       
      } else {
        const dataInfor = await playragnarokonlinebr(dataItem); 
        if (dataInfor === "") {
          result.push(await divinepride(dataItem));
        }else{
          result.push(dataInfor);
        }
        
      }
      console.log("====================================");
      console.log("dataItem: ", dataItem.id);
      console.log("jsonData  e result: ", result.length - jsonData.length);
      console.log("====================================");
      await sleep(800);
    }

    // Converte o objeto em uma string JSON
    const dadosJSON = JSON.stringify(result, null, 2);

    // Salva a string JSON em um arquivo
    fs.writeFile(data_infor_new, dadosJSON, "utf8", (err) => {
      if (err) {
        console.error("Erro ao salvar o arquivo JSON:", err);
      } else {
        console.log(`Arquivo JSON "${data_infor_new}" salvo com sucesso.`);
      }
    });
  });
})();
