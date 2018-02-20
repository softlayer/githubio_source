<div id="leftsidebar">
    <div class="sidebar-spacer">&nbsp;</div>
    <div class="region region-leftsidebar">
        <div id="block-menu-menu-reference-overview" class="block block-menu">
            <div class="content">
                <ul class="menu clearfix">
                    <li class="first leaf"><a href="/" title="">Examples</a></li>
                    <li class="leaf"><a href="/reference/softlayerapi" title="">SoftLayer API</a></li>
                    <li class="leaf"><a href="https://ibm-public-cos.github.io/crs-docs/using-the-api" title="">Object Storage API</a></li>
                    <li class="last leaf"><a href="https://console.bluemix.net/docs/" title="">Bluemix API</a></li>
                </ul>
            </div>
        </div> 
        <div id="block-views-data_types_list-block">
            <h2>Data Types</h2>
            <div class="content">
                <div class="view view-data-types-list">
                    <div class="view-header">
                        <strong>"SoftLayer_"</strong> prefix removed for readability.    
                    </div>
                </div>

<!-- Service Filer BEGIN -->
                        <div class="view-filters">
                            <form action="/" method="get" id="js-search-content" accept-charset="UTF-8" class="jquery-once-1-processed">
                                <div class="clearfix">
                                    <div class="search-input-box">
                                        <input placeholder="<?= $this->sidebar ?> Filter" onkeyup="titleSearch(inputId='list-input', divId='sidebar-list', elementClass='list-row')" 
                                            type="text" id="list-input" value="" size="20" maxlength="128" class="form-text">
                                    </div>
                                </div>
                            </form>
                        </div>

<!-- Service Filer END -->
                <div id="sidebar-list" >
                    <div class="list-row">
                        Services or Datatypes go here
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script> 
    $(function(){
        $("#sidebar-list").load("/reference/<?= $this->sidebar ?>/list.html"); 
    });
</script> 
