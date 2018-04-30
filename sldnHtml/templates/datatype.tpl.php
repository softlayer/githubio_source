<?= $this->render('header.tpl.php'); ?>
       <div class="section clearfix">
        <?php //print_r($this) ?>
        <div id="main-wrapper">

            <div id="main" class="clearfix">
                <?= $this->render('sidebar.tpl.php'); ?>
                <div id='content' class='inner-content'>
                    <h1 class='title' id='page-title'> 
                        <div id='title-category'><?= $this->category?> </div>
                        <div id='title-full'><?= $this->title ?></div>
                    </h1>
                    <div id='service-datatype'>
                        <ul id='sldn-reference-tabs'>
                        <?php if($this->checkForService()): ?><li id='service'> <a href='/reference/services/<?=$this->title?>' >Service</a></li><?php endif ?>
                        <li id='datatype'> <a href='/reference/datatypes/<?=$this->title?>' >Datatype</a></li>
                        </ul>
                    </div>
                    <h2> Description </h2>
                    <?= $this->body ?>
<!-- Service Filer BEGIN -->
                        <div class="view-filters">
                            <form action="/" method="get" id="js-search-content" accept-charset="UTF-8" class="jquery-once-1-processed">
                                <div class="clearfix">
                                    <div class="search-input-box">
                                        <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                                            type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
                                    </div>
                                </div>
                            </form>
                        </div>

<!-- Service Filer END -->
                    <div id="properties" class="content">
                        <div id="localProperties" class="prop-content" >
                            <h2>Local</h2>
                            <?php foreach($this->localProperties as $property): ?>
                            <div class='prop-row views-row'>
                                <span class='views-field-title'><a href="#<?=$property->title?>" name=<?=$property->title?>><?= $property->title ?></a></span>
                                <div class='views-field-body'><?= $property->body ?> </div>
                                <span class="type-label">Type:</span> <div class='type-content'><p><?= $this->print_property_type($property->classType, $property->isArray) ?></p></div>
                            </div>
                            <?php endforeach ?>
                        </div>
                        <?php if(count($this->relationalProperties) > 0): ?>
                        <div id="relationalProperties"  class="prop-content" >
                            <h2>Relational</h2>
                            <?php foreach($this->relationalProperties as $property): ?>
                            <div class='prop-row views-row'>
                                <span class='views-field-title'><a href="#<?=$property->title?>" name=<?=$property->title?>><?= $property->title ?></a></span>
                                <div class='views-field-body'><?= $property->body ?> </div>
                                <span class="type-label">Type:</span> <div class='type-content'><p><?= $this->print_property_type($property->classType, $property->isArray) ?></p></div>
                            </div>
                            <?php endforeach ?>
                        </div>
                    <?php endif?>
                    </div>

                    <br>

                </div> 
            </div>
        </div>
        </div>

    </body>
</html>