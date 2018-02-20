<?= $this->render('header.tpl.php'); ?>
        <div class="section clearfix">
        <div id="main-wrapper">
            <div id="main" class="clearfix">
            <?= $this->render('sidebar.tpl.php'); ?>
            <div id='content' class='inner-content'>

                    <h1 class='title' id='page-title'> 
                        <div id='title-category'><?= $this->title ?></div>
                    </h1>
                    <div id='service-datatype'>
                        <ul id='sldn-reference-tabs'>
                        <?php if($this->checkForService()): ?><li id='service'> <a href='/reference/services/<?=$this->title?>' >Service</a></li><?php endif ?>
                        <li id='datatype'> <a href='/reference/datatypes/<?=$this->title?>' >Datatype</a></li>
                        </ul>
                    </div>
                    <h2> Description </h2>
                    <?= $this->body ?>
                    <div id="properties" class="content">
                        <h2>Methods</h2>
<!-- Service Filer BEGIN -->
                        <div class="view-filters">
                            <form action="/" method="get" id="js-search-content" accept-charset="UTF-8" class="jquery-once-1-processed">
                                <div class="clearfix">
                                    <div class="search-input-box">
                                        <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                                            type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
                                    </div>
                                </div>
                            </form>
                        </div>

<!-- Service Filer END -->
                        <div id="method-div">
                        <?php foreach($this->methods as $method): ?>
                            <div class="method-row">
                                <?php $methodPath = '/reference/services/' . $this->title . '/' . $method->title . '.html'; ?>
                                <span class='view-field-title'><a href='<?=$methodPath?>'> <?= $method->title ?></a> </span>
                                <div class='views-field-body'><?= $method->shortDescription ?></div>
                            </div>
                        <?php endforeach ?>
                        </div>
                    </div>

            </div>
        </div>
        </div>
    </div>
    </body>
</html>