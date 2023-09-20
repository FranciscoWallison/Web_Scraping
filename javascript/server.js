import puppeteer from "puppeteer";
import fs from "fs";

(async () => {
  const jsonData = "./pt-br/top.json";
  const nomeDoArquivo = "top-en.json";
  let result = [];

  await fs.readFile(jsonData, "utf8", async (error, data) => {
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

    for (let index = 0; index < jsonData.length; index++) {
      const dataItem = jsonData[index];

      if (dataItem.id === 0) {
        continue;
      }

      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      const url = `https://playragnarokonlinebr.com/database/thor/equipamentos?page=1&nome=${dataItem.name}&slots=&tipo=`;

      console.log("url: ", url);

      // Navigate the page to a URL
      await page.goto(url);

      // const elements = await page.evaluate(() => {
      //   return {
      //     Identified: document
      //       .getElementsByClassName("entry-title")[0]
      //       .getElementsByTagName("small")[0].innerText,
      //     TypeItem: document
      //       .getElementsByClassName(
      //         "table table-bordered table-striped table-condensed table-full table-small-text"
      //       )[0]
      //       .getElementsByTagName("tr")[4]
      //       .getElementsByTagName("td")[0].innerText,
      //   };
      // });
      let elements;
      try {
        elements = await page.evaluate(() => {
          return {
            Identified: document
              .getElementsByClassName("equipamentos show")[0]
              .getElementsByTagName("a")[0]
              .href.split("equipamentos/detalhes/")[1],
            link: document
              .getElementsByClassName("equipamentos show")[0]
              .getElementsByTagName("a")[0].href,
          };
        });
      } catch (error) {
        console.log('====================================');
        console.info(error);
        console.log('====================================');
      }


      const returnedTarget = Object.assign(dataItem, elements);
      console.log(returnedTarget);
      result.push(returnedTarget);

      await browser.close();
      await sleep(1000);
    }
    // Converte o objeto em uma string JSON
    const dadosJSON = JSON.stringify(result, null, 2);

    // Salva a string JSON em um arquivo
    fs.writeFile(nomeDoArquivo, dadosJSON, "utf8", (err) => {
      if (err) {
        console.error("Erro ao salvar o arquivo JSON:", err);
      } else {
        console.log(`Arquivo JSON "${nomeDoArquivo}" salvo com sucesso.`);
      }
    });
  });
})();
